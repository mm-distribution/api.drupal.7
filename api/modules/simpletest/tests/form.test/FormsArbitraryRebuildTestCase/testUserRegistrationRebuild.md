# FormsArbitraryRebuildTestCase::testUserRegistrationRebuild()

- **Type:** Method
- **File:** [`modules/simpletest/tests/form.test`](../_file.md), lines 2140–2149 · [local source](../../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L2140-L2149)
- **Class:** [FormsArbitraryRebuildTestCase](../FormsArbitraryRebuildTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testUserRegistrationRebuild()
```

## Documentation

```text
Tests a basic rebuild with the user registration form.
```

## Code

```php
  function testUserRegistrationRebuild() {
    $edit = array(
      'name' => 'foo',
      'mail' => 'bar@example.com',
    );
    $this->drupalPost('user/register', $edit, 'Rebuild');
    $this->assertText('Form rebuilt.');
    $this->assertFieldByName('name', 'foo', 'Entered user name has been kept.');
    $this->assertFieldByName('mail', 'bar@example.com', 'Entered mail address has been kept.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
