# NumberFieldTestCase::setUp()

- **Type:** Method
- **File:** [`modules/field/modules/number/number.test`](../_file.md), lines 24–28 · [local source](../../../../../../../source/modules/field/modules/number/number.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.test#L24-L28)
- **Class:** [NumberFieldTestCase](../NumberFieldTestCase.md)
- **Module/theme:** number

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('field_test');
    $this->web_user = $this->drupalCreateUser(array('access field_test content', 'administer field_test content', 'administer content types', 'administer fields'));
    $this->drupalLogin($this->web_user);
  }
```

---
_Drupal 7.103 · [modules/field/modules/number/number.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/number/number.test) · Licensed GPL-2.0-or-later (see LICENSE)._
