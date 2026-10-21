# EntityFieldQueryTestCase::assertEntityFieldQuery()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_query.test`](../_file.md), lines 1648–1665 · [local source](../../../../../../source/modules/simpletest/tests/entity_query.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test#L1648-L1665)
- **Class:** [EntityFieldQueryTestCase](../EntityFieldQueryTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertEntityFieldQuery($query, $intended_results, $message, $ordered = FALSE)
```

## Documentation

```text
Fetches the results of an EntityFieldQuery and compares.

@param $query
  An EntityFieldQuery to run.
@param $intended_results
  A list of results, every entry is again a list, first being the entity
  type, the second being the entity_id.
@param $message
  The message to be displayed as the result of this test.
@param $ordered
  If FALSE then the result of EntityFieldQuery will match
  $intended_results even if the order is not the same. If TRUE then order
  should match too.
```

## Code

```php
  function assertEntityFieldQuery($query, $intended_results, $message, $ordered = FALSE) {
    $results = array();
    try {
      foreach ($query->execute() as $entity_type => $entity_ids) {
        foreach ($entity_ids as $entity_id => $stub_entity) {
          $results[] = array($entity_type, $entity_id);
        }
      }
      if (!isset($ordered) || !$ordered) {
        sort($results);
        sort($intended_results);
      }
      $this->assertEqual($results, $intended_results, $message);
    }
    catch (Exception $e) {
      $this->fail('Exception thrown: '. $e->getMessage());
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_query.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_query.test) · Licensed GPL-2.0-or-later (see LICENSE)._
