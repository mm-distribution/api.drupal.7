# taxonomy_term_feed()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.pages.inc`](_file.md), lines 79–88 · [local source](../../../../source/modules/taxonomy/taxonomy.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.pages.inc#L79-L88)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_term_feed($term)
```

## Documentation

```text
Generate the content feed for a taxonomy term.

@param $term
  The taxonomy term.
```

## Code

```php
function taxonomy_term_feed($term) {
  $channel['link'] = url('taxonomy/term/' . $term->tid, array('absolute' => TRUE));
  $channel['title'] = variable_get('site_name', 'Drupal') . ' - ' . $term->name;
  // Only display the description if we have a single term, to avoid clutter and confusion.
  // HTML will be removed from feed description.
  $channel['description'] = check_markup($term->description, $term->format, '', TRUE);
  $nids = taxonomy_select_nodes($term->tid, FALSE, variable_get('feed_default_items', 10));

  node_feed($nids, $channel);
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
