# simpletest_script_init()

- **Type:** Function
- **File:** [`scripts/run-tests.sh`](_file.md), lines 286–352 · [local source](../../../source/scripts/run-tests.sh) · [GitHub](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh#L286-L352)

## Signature

```php
function simpletest_script_init($server_software)
```

## Documentation

```text
Initialize script variables and perform general setup requirements.
```

## Code

```php
function simpletest_script_init($server_software) {
  global $args, $php;

  $host = 'localhost';
  $path = '';
  // Determine location of php command automatically, unless a command line argument is supplied.
  if (!empty($args['php'])) {
    $php = $args['php'];
  }
  elseif ($php_env = getenv('_')) {
    // '_' is an environment variable set by the shell. It contains the command that was executed.
    $php = $php_env;
  }
  elseif (defined('PHP_BINARY') && $php_env = PHP_BINARY) {
    // 'PHP_BINARY' specifies the PHP binary path during script execution. Available since PHP 5.4.
    $php = $php_env;
  }
  elseif ($sudo = getenv('SUDO_COMMAND')) {
    // 'SUDO_COMMAND' is an environment variable set by the sudo program.
    // Extract only the PHP interpreter, not the rest of the command.
    list($php, ) = explode(' ', $sudo, 2);
  }
  else {
    simpletest_script_print_error('Unable to automatically determine the path to the PHP interpreter. Supply the --php command line argument.');
    simpletest_script_help();
    exit(SIMPLETEST_SCRIPT_EXIT_FAILURE);
  }

  // Get URL from arguments.
  if (!empty($args['url'])) {
    $parsed_url = parse_url($args['url']);
    $host = $parsed_url['host'] . (isset($parsed_url['port']) ? ':' . $parsed_url['port'] : '');
    $path = isset($parsed_url['path']) ? $parsed_url['path'] : '';

    // If the passed URL schema is 'https' then setup the $_SERVER variables
    // properly so that testing will run under HTTPS.
    if ($parsed_url['scheme'] == 'https') {
      $_SERVER['HTTPS'] = 'on';
    }
  }

  $_SERVER['HTTP_HOST'] = $host;
  $_SERVER['REMOTE_ADDR'] = '127.0.0.1';
  $_SERVER['SERVER_ADDR'] = '127.0.0.1';
  $_SERVER['SERVER_SOFTWARE'] = $server_software;
  $_SERVER['SERVER_NAME'] = 'localhost';
  $_SERVER['REQUEST_URI'] = $path .'/';
  $_SERVER['REQUEST_METHOD'] = 'GET';
  $_SERVER['SCRIPT_NAME'] = $path .'/index.php';
  $_SERVER['PHP_SELF'] = $path .'/index.php';
  $_SERVER['HTTP_USER_AGENT'] = 'Drupal command line';

  if (!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] == 'on') {
    // Ensure that any and all environment variables are changed to https://.
    foreach ($_SERVER as $key => $value) {
      // The first time this script runs $_SERVER['SERVER_SOFTWARE'] will be
      // NULL, so avoid errors from str_replace().
      if (!empty($_SERVER[$key])) {
        $_SERVER[$key] = str_replace('http://', 'https://', $_SERVER[$key]);
      }
    }
  }

  chdir(realpath(dirname(__FILE__) . '/..'));
  define('DRUPAL_ROOT', getcwd());
  require_once DRUPAL_ROOT . '/includes/bootstrap.inc';
}
```

---
_Drupal 7.103 · [scripts/run-tests.sh](https://github.com/drupal/drupal/blob/7.103/scripts/run-tests.sh) · Licensed GPL-2.0-or-later (see LICENSE)._
