# SelectQueryExtender::execute()

- **Type:** Method
- **File:** [`includes/database/select.inc`](../_file.md), lines 716–725 · [local source](../../../../../source/includes/database/select.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc#L716-L725)
- **Class:** [SelectQueryExtender](../SelectQueryExtender.md)
- **Topics:** [database](../../../../topics/database.md)

## Signature

```php
public function execute()
```

## Documentation

_No docblock in source._

## Code

```php
  public function execute() {
    // By calling preExecute() here, we force it to preprocess the extender
    // object rather than just the base query object.  That means
    // hook_query_alter() gets access to the extended object.
    if (!$this->preExecute($this)) {
      return NULL;
    }

    return $this->query->execute();
  }
```

---
_Drupal 7.103 · [includes/database/select.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/select.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
