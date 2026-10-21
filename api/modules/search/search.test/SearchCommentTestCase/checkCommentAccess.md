# SearchCommentTestCase::checkCommentAccess()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 928–942 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L928-L942)
- **Class:** [SearchCommentTestCase](../SearchCommentTestCase.md)
- **Module/theme:** search

## Signature

```php
function checkCommentAccess($message, $assume_access = FALSE)
```

## Documentation

```text
Update search index and search for comment.
```

## Code

```php
  function checkCommentAccess($message, $assume_access = FALSE) {
    // Invoke search index update.
    search_touch_node($this->node->nid);
    $this->cronRun();

    // Search for the comment subject.
    $edit = array(
      'search_block_form' => "'" . $this->comment_subject . "'",
    );
    $this->drupalPost('', $edit, t('Search'));
    $method = $assume_access ? 'assertText' : 'assertNoText';
    $verb = $assume_access ? 'found' : 'not found';
    $this->{$method}($this->node->title, "Node $verb in search results: " . $message);
    $this->{$method}($this->comment_subject, "Comment subject $verb in search results: " . $message);
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
