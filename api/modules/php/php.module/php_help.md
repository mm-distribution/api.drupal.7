# php_help()

- **Type:** Function
- **File:** [`modules/php/php.module`](_file.md), lines 11–24 · [local source](../../../../source/modules/php/php.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/php/php.module#L11-L24)
- **Module/theme:** php
- **Implements:** [hook_help()](../../system/system.api.php/hook_help.md)

## Signature

```php
function php_help($path, $arg)
```

## Documentation

```text
Implements hook_help().
```

## Code

```php
function php_help($path, $arg) {
  switch ($path) {
    case 'admin/help#php':
      $output = '';
      $output .= '<h3>' . t('About') . '</h3>';
      $output .= '<p>' . t('The PHP filter module adds a PHP filter to your site, for use with <a href="@filter">text formats</a>. This filter adds the ability to execute PHP code in any text field that uses a text format (such as the body of a content item or the text of a comment). <a href="@php-net">PHP</a> is a general-purpose scripting language widely-used for web development, and is the language with which Drupal has been developed. For more information, see the online handbook entry for the <a href="@php">PHP filter module</a>.', array('@filter' => url('admin/help/filter'), '@php-net' => 'http://www.php.net', '@php' => 'http://drupal.org/documentation/modules/php/')) . '</p>';
      $output .= '<h3>' . t('Uses') . '</h3>';
      $output .= '<dl>';
      $output .= '<dt>' . t('Enabling execution of PHP in text fields') . '</dt>';
      $output .= '<dd>' . t('The PHP filter module allows users with the proper permissions to include custom PHP code that will get executed when pages of your site are processed. While this is a powerful and flexible feature if used by a trusted user with PHP experience, it is a significant and dangerous security risk in the hands of a malicious or inexperienced user. Even a trusted user may accidentally compromise the site by entering malformed or incorrect PHP code. Only the most trusted users should be granted permission to use the PHP filter, and all PHP code added through the PHP filter should be carefully examined before use. <a href="@php-snippets">Example PHP snippets</a> can be found on Drupal.org.', array('@php-snippets' => url('http://drupal.org/documentation/customization/php-snippets'))) . '</dd>';
      $output .= '</dl>';
      return $output;
  }
}
```

---
_Drupal 7.103 · [modules/php/php.module](https://github.com/drupal/drupal/blob/7.103/modules/php/php.module) · Licensed GPL-2.0-or-later (see LICENSE)._
