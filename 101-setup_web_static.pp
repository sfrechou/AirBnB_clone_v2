# Redo the task #0 but by using Puppet
package { 'nginx':
  ensure   => installed,
  provider => 'apt',
  name     => 'nginx',
}

exec {'mkdir':
  command  => 'mkdir -p data/; mkdir -p data/web_static;
               mkdir -p /data/web_static/releases/; mkdir -p /data/web_static/shared/;
               mkdir -p /data/web_static/releases/test/',
  provider => 'shell',
}

exec {'echo':
  command  => 'echo "test_text" > /data/web_static/releases/test/index.html',
  provider => 'shell',
  requided => 'mkdir',
}

exec {'ln':
  command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => 'shell',
  requided => 'echo',
}

exec {'chown':
  command  => 'chown -R ubuntu:ubuntu /data/',
  provider => 'shell',
  requided => 'ln',
}

exec {'sed':
  command  => 'sed -i "37i\ location /hbnb_static/ { \n\t alias /data/web_static/current/ ; \n }" /etc/nginx/sites-available/default;
               service nginx restart',
  provider => 'shell',
  requided => 'chown',
}

service { 'nginx':
  ensure  => 'running',
}
