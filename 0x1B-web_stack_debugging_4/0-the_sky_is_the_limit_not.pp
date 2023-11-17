file { '/etc/default/nginx':
  ensure  => file,
  content => 'ULIMIT="-n 4096"\n',
}

exec { 'restart_nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => File['/etc/default/nginx'],
}
