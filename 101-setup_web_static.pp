# Puppet server setup

$html = "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>\n"
$root_path = '/data/web_static/'
$path_arr = ["${root_path}releases/test", "${root_path}shared"]

exec { 'update':
  command => '/usr/bin/apt-get update'
}

package { 'nginx':
  ensure  => installed
}

file { $path_arr:
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu'
}

file { "${root_path}releases/test/index.html":
  content => $html,
    owner => 'ubuntu',
    group => 'ubuntu'
}

file { "${root_path}current":
  ensure => 'link',
  target => "${root_path}releases/test/",
  force  => yes,
  owner  => 'ubuntu',
  group  => 'ubuntu'
}

exec { 'sed':
  command => '/usr/bin/env sed -i "/listen 80 default_server;/a \
\\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\
\n\t}\n" /etc/nginx/sites-available/default',
  require => Package['nginx']
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
