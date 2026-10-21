# FormsArbitraryRebuildTestCase::testUserRegistrationMultipleField()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 2154–2163 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L2154-L2163)
- **Class:** [FormsArbitraryRebuildTestCase](../FormsArbitraryRebuildTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testUserRegistrationMultipleField()
```

## Documentation

```text
Tests a rebuild caused by a multiple value field.
```

## Code

```php
  function testUserRegistrationMultipleField() {
    $edit = array(
      'name' => 'foo',
      'mail' => 'bar@example.com',
    );
    $this->drupalPost('user/register', $edit, t('Add another item'), array('query' => array('field' => TRUE)));
    $this->assertText('Test a multiple valued field', 'Form has been rebuilt.');
    $this->assertFieldByName('name', 'foo', 'Entered user name has been kept.');
    $this->assertFieldByName('mail', 'bar@example.com', 'Entered mail address has been kept.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
