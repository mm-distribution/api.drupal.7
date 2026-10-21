# color_requirements()

- **Type:** Function
- **File:** [`modules/color/color.install`](_file.md), lines 11–42 · [local source](../../../../source/modules/color/color.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.install#L11-L42)
- **Module/theme:** color
- **Implements:** [hook_requirements()](../../system/system.api.php/hook_requirements.md)

## Signature

```php
function color_requirements($phase)
```

## Documentation

```text
Implements hook_requirements().
```

## Code

```php
function color_requirements($phase) {
  $requirements = array();

  if ($phase == 'runtime') {
    // Check for the PHP GD library.
    if (function_exists('imagegd2')) {
      $info = gd_info();
      $requirements['color_gd'] = array(
        'value' => $info['GD Version'],
      );

      // Check for PNG support.
      if (function_exists('imagecreatefrompng')) {
        $requirements['color_gd']['severity'] = REQUIREMENT_OK;
      }
      else {
        $requirements['color_gd']['severity'] = REQUIREMENT_WARNING;
        $requirements['color_gd']['description'] = t('The GD library for PHP is enabled, but was compiled without PNG support. Check the <a href="@url">PHP image documentation</a> for information on how to correct this.', array('@url' => 'http://www.php.net/manual/ref.image.php'));
      }
    }
    else {
      $requirements['color_gd'] = array(
        'value' => t('Not installed'),
        'severity' => REQUIREMENT_ERROR,
        'description' => t('The GD library for PHP is missing or outdated. Check the <a href="@url">PHP image documentation</a> for information on how to correct this.', array('@url' => 'http://www.php.net/manual/book.image.php')),
      );
    }
    $requirements['color_gd']['title'] = t('GD library PNG support');
  }

  return $requirements;
}
```

---
_Drupal 7.103 · [modules/color/color.install](https://github.com/drupal/drupal/blob/7.103/modules/color/color.install) · Licensed GPL-2.0-or-later (see LICENSE)._
