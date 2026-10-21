# ForumTestCase::verifyForumView()

- **Type:** Method
- **File:** [`modules/forum/forum.test`](../_file.md), lines 619–634 · [local source](../../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L619-L634)
- **Class:** [ForumTestCase](../ForumTestCase.md)
- **Module/theme:** forum

## Signature

```php
private function verifyForumView($forum, $parent = NULL)
```

## Documentation

```text
Verifies display of forum page.

@param $forum
  A row from the taxonomy_term_data table in an array.
@param $parent
  (optional) An array representing the forum's parent.
```

## Code

```php
  private function verifyForumView($forum, $parent = NULL) {
    // View forum page.
    $this->drupalGet('forum/' . $forum['tid']);
    $this->assertResponse(200);
    $this->assertTitle($forum['name'] . ' | Drupal', 'Forum name was displayed');

    $breadcrumb = array(
      l(t('Home'), NULL),
      l(t('Forums'), 'forum'),
    );
    if (isset($parent)) {
      $breadcrumb[] = l($parent['name'], 'forum/' . $parent['tid']);
    }

    $this->assertRaw(theme('breadcrumb', array('breadcrumb' => $breadcrumb)), 'Breadcrumbs were displayed');
  }
```

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
