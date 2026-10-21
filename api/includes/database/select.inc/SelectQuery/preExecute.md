# SelectQuery::preExecute()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 1252–1301 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L1252-L1301)
- **Class:** [SelectQuery](../SelectQuery.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function preExecute(SelectQueryInterface $query = NULL)
```

## Documentation

```text
Generic preparation and validation for a SELECT query.

@return
  TRUE if the validation was successful, FALSE if not.
```

## Code

```php
  public function preExecute(SelectQueryInterface $query = NULL) {
    // If no query object is passed in, use $this.
    if (!isset($query)) {
      $query = $this;
    }

    // Only execute this once.
    if ($query->isPrepared()) {
      return TRUE;
    }

    // Modules may alter all queries or only those having a particular tag.
    if (isset($this->alterTags)) {
      // Many contrib modules assume that query tags used for access-checking
      // purposes follow the pattern $entity_type . '_access'. But this is
      // not the case for taxonomy terms, since core used to add term_access
      // instead of taxonomy_term_access to its queries. Provide backwards
      // compatibility by adding both tags here instead of attempting to fix
      // all contrib modules in a coordinated effort.
      // TODO:
      // - Extract this mechanism into a hook as part of a public (non-security)
      //   issue.
      // - Emit E_USER_DEPRECATED if term_access is used.
      //   https://www.drupal.org/node/2575081
      $term_access_tags = array('term_access' => 1, 'taxonomy_term_access' => 1);
      if (array_intersect_key($this->alterTags, $term_access_tags)) {
        $this->alterTags += $term_access_tags;
      }
      $hooks = array('query');
      foreach ($this->alterTags as $tag => $value) {
        $hooks[] = 'query_' . $tag;
      }
      drupal_alter($hooks, $query);
    }

    $this->prepared = TRUE;

    // Now also prepare any sub-queries.
    foreach ($this->tables as $table) {
      if ($table['table'] instanceof SelectQueryInterface) {
        $table['table']->preExecute();
      }
    }

    foreach ($this->union as $union) {
      $union['query']->preExecute();
    }

    return $this->prepared;
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
