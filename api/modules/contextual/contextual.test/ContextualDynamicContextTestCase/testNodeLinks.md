# ContextualDynamicContextTestCase::testNodeLinks()

- **Type:** Method
- **File:** [`modules/contextual/contextual.test`](../_file.md), lines 33–48 · [local source](../../../../../source/modules/contextual/contextual.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.test#L33-L48)
- **Class:** [ContextualDynamicContextTestCase](../ContextualDynamicContextTestCase.md)
- **Module/theme:** contextual

## Signature

```php
function testNodeLinks()
```

## Documentation

```text
Tests contextual links on node lists with different permissions.
```

## Code

```php
  function testNodeLinks() {
    // Create three nodes in the following order:
    // - An article, which should be user-editable.
    // - A page, which should not be user-editable.
    // - A second article, which should also be user-editable.
    $node1 = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1));
    $node2 = $this->drupalCreateNode(array('type' => 'page', 'promote' => 1));
    $node3 = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1));

    // Now, on the front page, all article nodes should have contextual edit
    // links. The page node in between should not.
    $this->drupalGet('node');
    $this->assertRaw('node/' . $node1->nid . '/edit', 'Edit link for oldest article node showing.');
    $this->assertNoRaw('node/' . $node2->nid . '/edit', 'No edit link for page nodes.');
    $this->assertRaw('node/' . $node3->nid . '/edit', 'Edit link for most recent article node showing.');
  }
```

---
_Drupal 7.103 · [modules/contextual/contextual.test](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.test) · Licensed GPL-2.0-or-later (see LICENSE)._
