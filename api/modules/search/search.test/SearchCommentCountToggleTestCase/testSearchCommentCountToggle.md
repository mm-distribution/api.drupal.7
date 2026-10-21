# SearchCommentCountToggleTestCase::testSearchCommentCountToggle()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1102–1132 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1102-L1132)
- **Class:** [SearchCommentCountToggleTestCase](../SearchCommentCountToggleTestCase.md)
- **Module/theme:** search

## Signature

```php
function testSearchCommentCountToggle()
```

## Documentation

```text
Verify that comment count display toggles properly on comment status of node
```

## Code

```php
  function testSearchCommentCountToggle() {
    // Search for the nodes by string in the node body.
    $edit = array(
      'search_block_form' => "'SearchCommentToggleTestCase'",
    );

    // Test comment count display for nodes with comment status set to Open
    $this->drupalPost('', $edit, t('Search'));
    $this->assertText(t('0 comments'), 'Empty comment count displays for nodes with comment status set to Open');
    $this->assertText(t('1 comment'), 'Non-empty comment count displays for nodes with comment status set to Open');

    // Test comment count display for nodes with comment status set to Closed
    $this->searchable_nodes['0 comments']->comment = COMMENT_NODE_CLOSED;
    node_save($this->searchable_nodes['0 comments']);
    $this->searchable_nodes['1 comment']->comment = COMMENT_NODE_CLOSED;
    node_save($this->searchable_nodes['1 comment']);

    $this->drupalPost('', $edit, t('Search'));
    $this->assertNoText(t('0 comments'), 'Empty comment count does not display for nodes with comment status set to Closed');
    $this->assertText(t('1 comment'), 'Non-empty comment count displays for nodes with comment status set to Closed');

    // Test comment count display for nodes with comment status set to Hidden
    $this->searchable_nodes['0 comments']->comment = COMMENT_NODE_HIDDEN;
    node_save($this->searchable_nodes['0 comments']);
    $this->searchable_nodes['1 comment']->comment = COMMENT_NODE_HIDDEN;
    node_save($this->searchable_nodes['1 comment']);

    $this->drupalPost('', $edit, t('Search'));
    $this->assertNoText(t('0 comments'), 'Empty comment count does not display for nodes with comment status set to Hidden');
    $this->assertNoText(t('1 comment'), 'Non-empty comment count does not display for nodes with comment status set to Hidden');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
