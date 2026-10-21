# search_update_totals()

- **Type:** Function
- **File:** [`modules/search/search.module`](_file.md), lines 373–398 · [local source](../../../../source/modules/search/search.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module#L373-L398)
- **Module/theme:** search

## Signature

```php
function search_update_totals()
```

## Documentation

```text
Updates the {search_total} database table.

This function is called on shutdown to ensure that {search_total} is always
up to date (even if cron times out or otherwise fails).
```

## Code

```php
function search_update_totals() {
  // Update word IDF (Inverse Document Frequency) counts for new/changed words.
  foreach (search_dirty() as $word => $dummy) {
    // Get total count
    $total = db_query("SELECT SUM(score) FROM {search_index} WHERE word = :word", array(':word' => $word), array('target' => 'slave'))->fetchField();
    // Apply Zipf's law to equalize the probability distribution.
    $total = log10(1 + 1/(max(1, $total)));
    db_merge('search_total')
      ->key(array('word' => $word))
      ->fields(array('count' => $total))
      ->execute();
  }
  // Find words that were deleted from search_index, but are still in
  // search_total. We use a LEFT JOIN between the two tables and keep only the
  // rows which fail to join.
  $result = db_query("SELECT t.word AS realword, i.word FROM {search_total} t LEFT JOIN {search_index} i ON t.word = i.word WHERE i.word IS NULL", array(), array('target' => 'slave'));
  $or = db_or();
  foreach ($result as $word) {
    $or->condition('word', $word->realword);
  }
  if (count($or) > 0) {
    db_delete('search_total')
      ->condition($or)
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/search/search.module](https://github.com/drupal/drupal/blob/7.103/modules/search/search.module) · Licensed GPL-2.0-or-later (see LICENSE)._
