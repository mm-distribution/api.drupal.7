# ForumTestCase::deleteForum()

- **Type:** Method
- **File:** [`modules/forum/forum.test`](../_file.md), lines 447–460 · [local source](../../../../../source/modules/forum/forum.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test#L447-L460)
- **Class:** [ForumTestCase](../ForumTestCase.md)
- **Module/theme:** forum

## Signature

```php
function deleteForum($tid)
```

## Documentation

```text
Deletes a forum.

@param $tid
  The forum ID.
```

## Code

```php
  function deleteForum($tid) {
    // Delete the forum.
    $this->drupalPost('admin/structure/forum/edit/forum/' . $tid, array(), t('Delete'));
    $this->drupalPost(NULL, array(), t('Delete'));

    // Assert that the forum no longer exists.
    $this->drupalGet('forum/' . $tid);
    $this->assertResponse(404, 'The forum was not found');

    // Assert that the associated term has been removed from the
    // forum_containers variable.
    $containers = variable_get('forum_containers', array());
    $this->assertFalse(in_array($tid, $containers), 'The forum_containers variable has been updated.');
  }
```

---
_Drupal 7.103 · [modules/forum/forum.test](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.test) · Licensed GPL-2.0-or-later (see LICENSE)._
