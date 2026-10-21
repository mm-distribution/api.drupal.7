# list_update_7002()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.install`](_file.md), lines 134–141 · [local source](../../../../../../source/modules/field/modules/list/list.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.install#L134-L141)
- **Module/theme:** list
- **Topics:** [updates-7.x-extra](../../../../../topics/updates-7.x-extra.md)

## Signature

```php
function list_update_7002()
```

## Documentation

```text
Re-apply list_update_7001() for deleted fields.
```

## Code

```php
function list_update_7002() {
  // See http://drupal.org/node/1022924: list_update_7001() intitally
  // overlooked deleted fields, which then caused fatal errors when the fields
  // were being purged.
  // list_update_7001() has the required checks to ensure it is reentrant, so
  // it can simply be executed once more..
  list_update_7001();
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.install](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.install) · Licensed GPL-2.0-or-later (see LICENSE)._
