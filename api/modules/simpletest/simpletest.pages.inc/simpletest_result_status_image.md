# simpletest_result_status_image()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.pages.inc`](_file.md), lines 414–430 · [local source](../../../../source/modules/simpletest/simpletest.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc#L414-L430)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_result_status_image($status)
```

## Documentation

```text
Get the appropriate image for the status.

@param $status Status string, either: pass, fail, exception.
@return HTML image or false.
```

## Code

```php
function simpletest_result_status_image($status) {
  // $map does not use drupal_static() as its value never changes.
  static $map;

  if (!isset($map)) {
    $map = array(
      'pass' => theme('image', array('path' => 'misc/watchdog-ok.png', 'width' => 18, 'height' => 18, 'alt' => t('Pass'))),
      'fail' => theme('image', array('path' => 'misc/watchdog-error.png', 'width' => 18, 'height' => 18, 'alt' => t('Fail'))),
      'exception' => theme('image', array('path' => 'misc/watchdog-warning.png', 'width' => 18, 'height' => 18, 'alt' => t('Exception'))),
      'debug' => theme('image', array('path' => 'misc/watchdog-warning.png', 'width' => 18, 'height' => 18, 'alt' => t('Debug'))),
    );
  }
  if (isset($map[$status])) {
    return $map[$status];
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
