# system_authorized_batch_process()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 1866–1870 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L1866-L1870)
- **Module/theme:** system
- **Topics:** [authorize](../../../topics/authorize.md)

## Signature

```php
function system_authorized_batch_process()
```

## Documentation

```text
Use authorize.php to run batch_process().

@see batch_process()
```

## Code

```php
function system_authorized_batch_process() {
  $finish_url = system_authorized_get_url();
  $process_url = system_authorized_batch_processing_url();
  batch_process($finish_url, $process_url);
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
