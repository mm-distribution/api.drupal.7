# system_authorized_run()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 1856–1859 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L1856-L1859)
- **Module/theme:** system
- **Topics:** [authorize](../../../topics/authorize.md)

## Signature

```php
function system_authorized_run($callback, $file, $arguments = array(), $page_title = NULL)
```

## Documentation

```text
Setup and invoke an operation using authorize.php.

@see system_authorized_init()
```

## Code

```php
function system_authorized_run($callback, $file, $arguments = array(), $page_title = NULL) {
  system_authorized_init($callback, $file, $arguments, $page_title);
  drupal_goto(system_authorized_get_url());
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
