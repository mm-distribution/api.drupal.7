# image_requirements()

- **Type:** Function
- **File:** [`modules/image/image.install`](_file.md), lines 491–522 · [local source](../../../../source/modules/image/image.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install#L491-L522)
- **Module/theme:** image
- **Implements:** [hook_requirements()](../../system/system.api.php/hook_requirements.md)

## Signature

```php
function image_requirements($phase)
```

## Documentation

```text
Implements hook_requirements() to check the PHP GD Library.

@param $phase
```

## Code

```php
function image_requirements($phase) {
  $requirements = array();

  if ($phase == 'runtime') {
    // Check for the PHP GD library.
    if (function_exists('imagegd2')) {
      $info = gd_info();
      $requirements['image_gd'] = array(
        'value' => $info['GD Version'],
      );

      // Check for filter and rotate support.
      if (function_exists('imagefilter') && function_exists('imagerotate')) {
        $requirements['image_gd']['severity'] = REQUIREMENT_OK;
      }
      else {
        $requirements['image_gd']['severity'] = REQUIREMENT_WARNING;
        $requirements['image_gd']['description'] = t('The GD Library for PHP is enabled, but was compiled without support for functions used by the rotate and desaturate effects. It was probably compiled using the official GD libraries from http://www.libgd.org instead of the GD library bundled with PHP. You should recompile PHP --with-gd using the bundled GD library. See <a href="http://www.php.net/manual/book.image.php">the PHP manual</a>.');
      }
    }
    else {
      $requirements['image_gd'] = array(
        'value' => t('Not installed'),
        'severity' => REQUIREMENT_ERROR,
        'description' => t('The GD library for PHP is missing or outdated. Check the <a href="@url">PHP image documentation</a> for information on how to correct this.', array('@url' => 'http://www.php.net/manual/book.image.php')),
      );
    }
    $requirements['image_gd']['title'] = t('GD library rotate and desaturate effects');
  }

  return $requirements;
}
```

---
_Drupal 7.103 · [modules/image/image.install](https://github.com/drupal/drupal/blob/7.103/modules/image/image.install) · Licensed GPL-2.0-or-later (see LICENSE)._
