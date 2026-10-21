# update_refresh()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 468–471 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L468-L471)
- **Module/theme:** update

## Signature

```php
function update_refresh()
```

## Documentation

```text
Refreshes the release data after loading the necessary include file.

@see _update_refresh()
```

## Code

```php
function update_refresh() {
  module_load_include('inc', 'update', 'update.fetch');
  return _update_refresh();
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
