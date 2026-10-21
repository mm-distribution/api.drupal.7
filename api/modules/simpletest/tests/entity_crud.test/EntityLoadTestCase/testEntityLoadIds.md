# EntityLoadTestCase::testEntityLoadIds()

- **Type:** Method
- **File:** [`modules/simpletest/tests/entity_crud.test`](../_file.md), lines 50–60 · [local source](../../../../../../source/modules/simpletest/tests/entity_crud.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud.test#L50-L60)
- **Class:** [EntityLoadTestCase](../EntityLoadTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testEntityLoadIds()
```

## Documentation

_No docblock in source._

## Code

```php
  public function testEntityLoadIds() {
    $this->drupalCreateNode(array('title' => 'Node 1'));
    $this->drupalCreateNode(array('title' => 'Node 2'));

    $nodes_loaded = entity_load('node', array('1', '2'));
    $this->assertEqual(count($nodes_loaded), 2);

    // Ensure that an id with a trailing decimal place is ignored.
    $nodes_loaded = entity_load('node', array('1.', '2'));
    $this->assertEqual(count($nodes_loaded), 1);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/entity_crud.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/entity_crud.test) · Licensed GPL-2.0-or-later (see LICENSE)._
