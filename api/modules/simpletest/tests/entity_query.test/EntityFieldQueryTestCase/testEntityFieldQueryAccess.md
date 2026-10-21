# EntityFieldQueryTestCase::testEntityFieldQueryAccess()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_query.test`](../_file.md), lines 1616–1631 · [local source](../../../../../../source/modules/simpletest/tests/entity_query.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test#L1616-L1631)
- **Class:** [EntityFieldQueryTestCase](../EntityFieldQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testEntityFieldQueryAccess()
```

## Documentation

```text
Tests EntityFieldQuery access on non-node entities.
```

## Code

```php
  function testEntityFieldQueryAccess() {
    // Test as a user with ability to bypass node access.
    $privileged_user = $this->drupalCreateUser(array('bypass node access', 'access content'));
    $this->drupalLogin($privileged_user);
    $this->drupalGet('entity-query-access/test/' . $this->fields[0]['field_name']);
    $this->assertText('Found entity', 'Returned access response with entities.');
    $this->drupalLogout();

    // Test as a user that does not have ability to bypass node access or view
    // all nodes.
    $regular_user = $this->drupalCreateUser(array('access content'));
    $this->drupalLogin($regular_user);
    $this->drupalGet('entity-query-access/test/' . $this->fields[0]['field_name']);
    $this->assertText('Found entity', 'Returned access response with entities.');
    $this->drupalLogout();
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_query.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test) · Licensed GPL-2.0-or-later (see LICENSE)._
