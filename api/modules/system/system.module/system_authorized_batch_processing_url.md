# system_authorized_batch_processing_url()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 1847–1849 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L1847-L1849)
- **Module/theme:** system
- **Topics:** [authorize](../../../topics/authorize.md)

## Signature

```php
function system_authorized_batch_processing_url()
```

## Documentation

```text
Returns the URL for the authorize.php script when it is processing a batch.
```

## Code

```php
function system_authorized_batch_processing_url() {
  return system_authorized_get_url(array('query' => array('batch' => '1')));
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
