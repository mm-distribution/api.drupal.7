# TextFieldTestCase::setUp()

- **Type:** Method
- **File:** [`modules/field/modules/text/text.test`](../_file.md), lines 23–29 · [local source](../../../../../../../source/modules/field/modules/text/text.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test#L23-L29)
- **Class:** [TextFieldTestCase](../TextFieldTestCase.md)
- **Module/theme:** text

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

    $this->admin_user = $this->drupalCreateUser(array('administer filters'));
    $this->web_user = $this->drupalCreateUser(array('access field_test content', 'administer field_test content'));
    $this->drupalLogin($this->web_user);
  }
```

---
_Drupal 7.103 · [modules/field/modules/text/text.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/text/text.test) · Licensed GPL-2.0-or-later (see LICENSE)._
