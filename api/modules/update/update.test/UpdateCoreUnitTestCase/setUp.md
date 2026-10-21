# UpdateCoreUnitTestCase::setUp()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 809–812 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L809-L812)
- **Class:** [UpdateCoreUnitTestCase](../UpdateCoreUnitTestCase.md)
- **Module/theme:** update

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('update');
    module_load_include('inc', 'update', 'update.fetch');
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
