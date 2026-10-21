# php_enable()

- **Type:** Function
- **File:** [`modules/php/php.install`](_file.md), lines 11–38 · [local source](../../../../source/modules/php/php.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/php/php.install#L11-L38)
- **Module/theme:** php
- **Implements:** [hook_enable()](../../system/system.api.php/hook_enable.md)

## Signature

```php
function php_enable()
```

## Documentation

```text
Implements hook_enable().
```

## Code

```php
function php_enable() {
  $format_exists = (bool) db_query_range('SELECT 1 FROM {filter_format} WHERE name = :name', 0, 1, array(':name' => 'PHP code'))->fetchField();
  // Add a PHP code text format, if it does not exist. Do this only for the
  // first install (or if the format has been manually deleted) as there is no
  // reliable method to identify the format in an uninstall hook or in
  // subsequent clean installs.
  if (!$format_exists) {
    $php_format = array(
      'format' => 'php_code',
      'name' => 'PHP code',
      // 'Plain text' format is installed with a weight of 10 by default. Use a
      // higher weight here to ensure that this format will not be the default
      // format for anyone.
      'weight' => 11,
      'filters' => array(
        // Enable the PHP evaluator filter.
        'php_code' => array(
          'weight' => 0,
          'status' => 1,
        ),
      ),
    );
    $php_format = (object) $php_format;
    filter_format_save($php_format);

    drupal_set_message(t('A <a href="@php-code">PHP code</a> text format has been created.', array('@php-code' => url('admin/config/content/formats/' . $php_format->format))));
  }
}
```

---
_Drupal 7.103 · [modules/php/php.install](https://github.com/drupal/drupal/blob/7.103/modules/php/php.install) · Licensed GPL-2.0-or-later (see LICENSE)._
