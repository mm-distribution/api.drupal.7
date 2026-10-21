# SearchCommentTestCase::testAddNewComment()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 947–978 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L947-L978)
- **Class:** [SearchCommentTestCase](../SearchCommentTestCase.md)
- **Module/theme:** search

## Signature

```php
function testAddNewComment()
```

## Documentation

```text
Verify that 'add new comment' does not appear in search results or index.
```

## Code

```php
  function testAddNewComment() {
    // Create a node with a short body.
    $settings = array(
      'type' => 'article',
      'title' => 'short title',
      'body' => array(LANGUAGE_NONE => array(array('value' => 'short body text'))),
    );

    $user = $this->drupalCreateUser(array('search content', 'create article content', 'access content'));
    $this->drupalLogin($user);

    $node = $this->drupalCreateNode($settings);
    // Verify that if you view the node on its own page, 'add new comment'
    // is there.
    $this->drupalGet('node/' . $node->nid);
    $this->assertText(t('Add new comment'), 'Add new comment appears on node page');

    // Run cron to index this page.
    $this->drupalLogout();
    $this->cronRun();

    // Search for 'comment'. Should be no results.
    $this->drupalLogin($user);
    $this->drupalPost('search/node', array('keys' => 'comment'), t('Search'));
    $this->assertText(t('Your search yielded no results'), 'No results searching for the word comment');

    // Search for the node title. Should be found, and 'Add new comment' should
    // not be part of the search snippet.
    $this->drupalPost('search/node', array('keys' => 'short'), t('Search'));
    $this->assertText($node->title, 'Search for keyword worked');
    $this->assertNoText(t('Add new comment'), 'Add new comment does not appear on search results page');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
