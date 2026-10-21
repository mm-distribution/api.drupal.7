# SearchCommentCountToggleTestCase::setUp()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 1065–1097 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L1065-L1097)
- **Class:** [SearchCommentCountToggleTestCase](../SearchCommentCountToggleTestCase.md)
- **Module/theme:** search

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('search');

    // Create searching user.
    $this->searching_user = $this->drupalCreateUser(array('search content', 'access content', 'access comments', 'skip comment approval'));

    // Create initial nodes.
    $node_params = array('type' => 'article', 'body' => array(LANGUAGE_NONE => array(array('value' => 'SearchCommentToggleTestCase'))));

    $this->searchable_nodes['1 comment'] = $this->drupalCreateNode($node_params);
    $this->searchable_nodes['0 comments'] = $this->drupalCreateNode($node_params);

    // Login with sufficient privileges.
    $this->drupalLogin($this->searching_user);

    // Create a comment array
    $edit_comment = array();
    $edit_comment['subject'] = $this->randomName();
    $edit_comment['comment_body[' . LANGUAGE_NONE . '][0][value]'] = $this->randomName();
    $filtered_html_format_id = 'filtered_html';
    $edit_comment['comment_body[' . LANGUAGE_NONE . '][0][format]'] = $filtered_html_format_id;

    // Post comment to the test node with comment
    $this->drupalPost('comment/reply/' . $this->searchable_nodes['1 comment']->nid, $edit_comment, t('Save'));

    // First update the index. This does the initial processing.
    node_update_index();

    // Then, run the shutdown function. Testing is a unique case where indexing
    // and searching has to happen in the same request, so running the shutdown
    // function manually is needed to finish the indexing process.
    search_update_totals();
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
