# simpletest_requirements()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.install`](_file.md), lines 16–59 · [local source](../../../../source/modules/simpletest/simpletest.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.install#L16-L59)
- **Module/theme:** simpletest
- **Implements:** [hook_requirements()](../../system/system.api.php/hook_requirements.md)

## Signature

```php
function simpletest_requirements($phase)
```

## Documentation

```text
Implements hook_requirements().
```

## Code

```php
function simpletest_requirements($phase) {
  $requirements = array();
  $t = get_t();

  $has_curl = function_exists('curl_init');
  $has_hash = function_exists('hash_hmac');
  $has_domdocument = method_exists('DOMDocument', 'loadHTML');

  $requirements['curl'] = array(
    'title' => $t('cURL'),
    'value' => $has_curl ? $t('Enabled') : $t('Not found'),
  );
  if (!$has_curl) {
    $requirements['curl']['severity'] = REQUIREMENT_ERROR;
    $requirements['curl']['description'] = $t('The testing framework could not be installed because the PHP <a href="@curl_url">cURL</a> library is not available.', array('@curl_url' => 'http://php.net/manual/en/curl.setup.php'));
  }
  $requirements['hash'] = array(
    'title' => $t('hash'),
    'value' => $has_hash ? $t('Enabled') : $t('Not found'),
  );
  if (!$has_hash) {
    $requirements['hash']['severity'] = REQUIREMENT_ERROR;
    $requirements['hash']['description'] = $t('The testing framework could not be installed because the PHP <a href="@hash_url">hash</a> extension is disabled.', array('@hash_url' => 'http://php.net/manual/en/book.hash.php'));
  }

  $requirements['php_domdocument'] = array(
    'title' => $t('PHP DOMDocument class'),
    'value' => $has_domdocument ? $t('Enabled') : $t('Not found'),
  );
  if (!$has_domdocument) {
    $requirements['php_domdocument']['severity'] = REQUIREMENT_ERROR;
    $requirements['php_domdocument']['description'] = $t('The testing framework requires the DOMDocument class to be available. Check the configure command at the <a href="@link-phpinfo">PHP info page</a>.', array('@link-phpinfo' => url('admin/reports/status/php')));
  }

  // Check the current memory limit. If it is set too low, SimpleTest will fail
  // to load all tests and throw a fatal error.
  $memory_limit = ini_get('memory_limit');
  if (!drupal_check_memory_limit(SIMPLETEST_MINIMUM_PHP_MEMORY_LIMIT, $memory_limit)) {
    $requirements['php_memory_limit']['severity'] = REQUIREMENT_ERROR;
    $requirements['php_memory_limit']['description'] = $t('The testing framework requires the PHP memory limit to be at least %memory_minimum_limit. The current value is %memory_limit. <a href="@url">Follow these steps to continue</a>.', array('%memory_limit' => $memory_limit, '%memory_minimum_limit' => SIMPLETEST_MINIMUM_PHP_MEMORY_LIMIT, '@url' => 'http://drupal.org/node/207036'));
  }

  return $requirements;
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.install](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.install) · Licensed GPL-2.0-or-later (see LICENSE)._
