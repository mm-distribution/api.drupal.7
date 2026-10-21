# SearchCommentTestCase::testSearchResultsComment()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 789–853 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L789-L853)
- **Class:** [SearchCommentTestCase](../SearchCommentTestCase.md)
- **Module/theme:** search

## Signature

```php
function testSearchResultsComment()
```

## Documentation

```text
Verify that comments are rendered using proper format in search results.
```

## Code

```php
  function testSearchResultsComment() {
    $comment_body = 'Test comment body';

    variable_set('comment_preview_article', DRUPAL_OPTIONAL);
    // Enable check_plain() for 'Filtered HTML' text format.
    $filtered_html_format_id = 'filtered_html';
    $edit = array(
      'filters[filter_html_escape][status]' => TRUE,
    );
    $this->drupalPost('admin/config/content/formats/' . $filtered_html_format_id, $edit, t('Save configuration'));
    // Allow anonymous users to search content.
    $edit = array(
      DRUPAL_ANONYMOUS_RID . '[search content]' => 1,
      DRUPAL_ANONYMOUS_RID . '[access comments]' => 1,
      DRUPAL_ANONYMOUS_RID . '[post comments]' => 1,
    );
    $this->drupalPost('admin/people/permissions', $edit, t('Save permissions'));

    // Create a node.
    $node = $this->drupalCreateNode(array('type' => 'article'));
    // Post a comment using 'Full HTML' text format.
    $edit_comment = array();
    $edit_comment['subject'] = 'Test comment subject';
    $edit_comment['comment_body[' . LANGUAGE_NONE . '][0][value]'] = '<h1>' . $comment_body . '</h1>';
    $full_html_format_id = 'full_html';
    $edit_comment['comment_body[' . LANGUAGE_NONE . '][0][format]'] = $full_html_format_id;
    $this->drupalPost('comment/reply/' . $node->nid, $edit_comment, t('Save'));

    // Invoke search index update.
    $this->drupalLogout();
    $this->cronRun();

    // Search for the comment subject.
    $edit = array(
      'search_block_form' => "'" . $edit_comment['subject'] . "'",
    );
    $this->drupalPost('', $edit, t('Search'));
    $this->assertText($node->title, 'Node found in search results.');
    $this->assertText($edit_comment['subject'], 'Comment subject found in search results.');

    // Search for the comment body.
    $edit = array(
      'search_block_form' => "'" . $comment_body . "'",
    );
    $this->drupalPost('', $edit, t('Search'));
    $this->assertText($node->title, 'Node found in search results.');

    // Verify that comment is rendered using proper format.
    $this->assertText($comment_body, 'Comment body text found in search results.');
    $this->assertNoRaw(t('n/a'), 'HTML in comment body is not hidden.');
    $this->assertNoRaw(check_plain($edit_comment['comment_body[' . LANGUAGE_NONE . '][0][value]']), 'HTML in comment body is not escaped.');

    // Hide comments.
    $this->drupalLogin($this->admin_user);
    $node->comment = 0;
    node_save($node);

    // Invoke search index update.
    $this->drupalLogout();
    $this->cronRun();

    // Search for $title.
    $this->drupalPost('', $edit, t('Search'));
    $this->assertNoText($comment_body, 'Comment body text not found in search results.');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
