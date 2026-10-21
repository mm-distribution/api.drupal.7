# PagerDefault::execute()

- **Type:** Method
- **File:** [`includes/pager.inc`](../_file.md), lines 59–80 · [local source](../../../../source/includes/pager.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc#L59-L80)
- **Class:** [PagerDefault](../PagerDefault.md)

## Signature

```php
public function execute()
```

## Documentation

```text
Override the execute method.

Before we run the query, we need to add pager-based range() instructions
to it.
```

## Code

```php
  public function execute() {

    // Add convenience tag to mark that this is an extended query. We have to
    // do this in the constructor to ensure that it is set before preExecute()
    // gets called.
    if (!$this->preExecute($this)) {
      return NULL;
    }

    // A NULL limit is the "kill switch" for pager queries.
    if (empty($this->limit)) {
      return;
    }
    $this->ensureElement();

    $total_items = $this->getCountQuery()->execute()->fetchField();
    $current_page = pager_default_initialize($total_items, $this->limit, $this->element);
    $this->range($current_page * $this->limit, $this->limit);

    // Now that we've added our pager-based range instructions, run the query normally.
    return $this->query->execute();
  }
```

---
_Drupal 7.103 · [includes/pager.inc](https://github.com/drupal/drupal/blob/7.103/includes/pager.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
