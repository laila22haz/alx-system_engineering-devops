# try  to replace the fix the extension error
file { '/var/www/html/wp-settings.php':
  ensure  => file,
  source  => '/var/www/html/wp-settings.php',
  replace => false,
}

exec { 'fix_wp_settings':
  command => 'sed -i "s/\.phpp/\.php/g" /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/bin'],
}
