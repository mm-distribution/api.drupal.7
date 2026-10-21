# _unicode_check()

- **Type:** Function
- **File:** [`includes/unicode.inc`](_file.md), lines 103–134 · [local source](../../../source/includes/unicode.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc#L103-L134)

## Signature

```php
function _unicode_check()
```

## Documentation

```text
Perform checks about Unicode support in PHP, and set the right settings if
needed.

Because Drupal needs to be able to handle text in various encodings, we do
not support mbstring function overloading. HTTP input/output conversion must
be disabled for similar reasons.

@param $errors
  Whether to report any fatal errors with form_set_error().
```

## Code

```php
function _unicode_check() {
  // Ensure translations don't break during installation.
  $t = get_t();

  // Check for mbstring extension
  if (!function_exists('mb_strlen')) {
    return array(UNICODE_SINGLEBYTE, $t('Operations on Unicode strings are emulated on a best-effort basis. Install the <a href="@url">PHP mbstring extension</a> for improved Unicode support.', array('@url' => 'http://www.php.net/mbstring')));
  }

  // Check mbstring configuration
  if (ini_get('mbstring.func_overload') != 0) {
    return array(UNICODE_ERROR, $t('Multibyte string function overloading in PHP is active and must be disabled. Check the php.ini <em>mbstring.func_overload</em> setting. Please refer to the <a href="@url">PHP mbstring documentation</a> for more information.', array('@url' => 'http://www.php.net/mbstring')));
  }
  if (ini_get('mbstring.encoding_translation') != 0) {
    return array(UNICODE_ERROR, $t('Multibyte string input conversion in PHP is active and must be disabled. Check the php.ini <em>mbstring.encoding_translation</em> setting. Please refer to the <a href="@url">PHP mbstring documentation</a> for more information.', array('@url' => 'http://www.php.net/mbstring')));
  }
  // mbstring.http_input and mbstring.http_output are deprecated and empty by
  // default in PHP 5.6.
  if (version_compare(PHP_VERSION, '5.6.0') == -1) {
    if (ini_get('mbstring.http_input') != 'pass') {
      return array(UNICODE_ERROR, $t('Multibyte string input conversion in PHP is active and must be disabled. Check the php.ini <em>mbstring.http_input</em> setting. Please refer to the <a href="@url">PHP mbstring documentation</a> for more information.', array('@url' => 'http://www.php.net/mbstring')));
    }
    if (ini_get('mbstring.http_output') != 'pass') {
      return array(UNICODE_ERROR, $t('Multibyte string output conversion in PHP is active and must be disabled. Check the php.ini <em>mbstring.http_output</em> setting. Please refer to the <a href="@url">PHP mbstring documentation</a> for more information.', array('@url' => 'http://www.php.net/mbstring')));
    }
  }

  // Set appropriate configuration
  mb_internal_encoding('utf-8');
  mb_language('uni');
  return array(UNICODE_MULTIBYTE, '');
}
```

---
_Drupal 7.103 · [includes/unicode.inc](https://github.com/drupal/drupal/blob/7.103/includes/unicode.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
