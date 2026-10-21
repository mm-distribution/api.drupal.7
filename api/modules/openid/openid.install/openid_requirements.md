# openid_requirements()

- **Type:** Function
- **File:** [`modules/openid/openid.install`](_file.md), lines 93–122 · [local source](../../../../source/modules/openid/openid.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.install#L93-L122)
- **Module/theme:** openid
- **Implements:** [hook_requirements()](../../system/system.api.php/hook_requirements.md)

## Signature

```php
function openid_requirements($phase)
```

## Documentation

```text
Implements hook_requirements().
```

## Code

```php
function openid_requirements($phase) {
  $requirements = array();

  if ($phase == 'runtime') {
    // Check for the PHP BC Math library.
    if (!function_exists('bcadd') && !function_exists('gmp_add')) {
      $requirements['openid_math'] = array(
        'value' => t('Not installed'),
        'severity' => REQUIREMENT_ERROR,
        'description' => t('OpenID suggests the use of either the <a href="@gmp">GMP Math</a> (recommended for performance) or <a href="@bc">BC Math</a> libraries to enable OpenID associations.', array('@gmp' => 'http://php.net/manual/en/book.gmp.php', '@bc' => 'http://www.php.net/manual/en/book.bc.php')),
      );
    }
    elseif (!function_exists('gmp_add')) {
      $requirements['openid_math'] = array(
        'value' => t('Not optimized'),
        'severity' => REQUIREMENT_WARNING,
        'description' => t('OpenID suggests the use of the GMP Math library for PHP for optimal performance. Check the <a href="@url">GMP Math Library documentation</a> for installation instructions.', array('@url' => 'http://www.php.net/manual/en/book.gmp.php')),
      );
    }
    else {
      $requirements['openid_math'] = array(
        'value' => t('Installed'),
        'severity' => REQUIREMENT_OK,
      );
    }
    $requirements['openid_math']['title'] = t('OpenID Math library');
  }

  return $requirements;
}
```

---
_Drupal 7.103 · [modules/openid/openid.install](https://github.com/drupal/drupal/blob/7.103/modules/openid/openid.install) · Licensed GPL-2.0-or-later (see LICENSE)._
