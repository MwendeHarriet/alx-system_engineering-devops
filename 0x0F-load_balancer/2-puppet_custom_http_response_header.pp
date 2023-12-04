# Custom http header in a nginx server with puppet

# Update ubuntu server
exec { 'update server':
  command  => 'apt-get update',
  user     => 'root',
  provider => 'shell',
}
->
# Perform nginx installation on server
package { 'nginx':
  ensure   => present,
  provider => 'apt'
}
->
# Custom hhtp header response X-Served-By: hostname
file_line { 'add HTTP header':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'add_header X-Served-By $hostname;'
}
->
# Commence
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx']
}
