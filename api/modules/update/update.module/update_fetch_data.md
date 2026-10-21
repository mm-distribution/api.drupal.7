# update_fetch_data()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 478–481 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L478-L481)
- **Module/theme:** update

## Signature

```php
function update_fetch_data()
```

## Documentation

```text
Attempts to fetch update data after loading the necessary include file.

@see _update_fetch_data()
```

## Code

```php
function update_fetch_data() {
  module_load_include('inc', 'update', 'update.fetch');
  return _update_fetch_data();
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
