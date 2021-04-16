# Redo the task #0 but by using Puppet
exec {'install':
  command  => 'apt-get update -y;
               apt-get install -y nginx',
  provider => 'shell',
}

exec {'mkdir':
  command  => 'mkdir -p data/; mkdir -p data/web_static;
               mkdir -p /data/web_static/releases/; mkdir -p /data/web_static/shared/;
               mkdir -p /data/web_static/releases/test/',
  provider => 'shell',
  require => Exec['install'],
}

exec {'echo':
  command  => 'echo "test_text" > /data/web_static/releases/test/index.html',
  provider => 'shell',
  require => Exec['mkdir'],
}

exec {'ln':
  command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
  provider => 'shell',
  require => Exec['echo'],
}

exec {'chown':
  command  => 'chown -R ubuntu:ubuntu /data/',
  provider => 'shell',
  require => Exec['ln'],
}

exec {'sed':
  command  => 'sed -i "37i\ location /hbnb_static/ { \n\t alias /data/web_static/current/ ; \n }" /etc/nginx/sites-available/default;
               service nginx restart',
  provider => 'shell',
  require => Exec['chown'],
}
