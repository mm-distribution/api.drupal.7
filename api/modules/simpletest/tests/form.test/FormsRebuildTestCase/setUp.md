# FormsRebuildTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 1737–1742 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1737-L1742)
- **Class:** [FormsRebuildTestCase](../FormsRebuildTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('form_test');

    $this->web_user = $this->drupalCreateUser(array('access content'));
    $this->drupalLogin($this->web_user);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
