# ImportOPMLTestCase::openImportForm()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 748–765 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L748-L765)
- **Class:** [ImportOPMLTestCase](../ImportOPMLTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function openImportForm()
```

## Documentation

```text
Opens OPML import form.
```

## Code

```php
  function openImportForm() {
    db_delete('aggregator_category')->execute();

    $category = $this->randomName(10);
    $cid = db_insert('aggregator_category')
      ->fields(array(
        'title' => $category,
        'description' => '',
      ))
      ->execute();

    $this->drupalGet('admin/config/services/aggregator/add/opml');
    $this->assertText('A single OPML document may contain a collection of many feeds.', 'Found OPML help text.');
    $this->assertField('files[upload]', 'Found file upload field.');
    $this->assertField('remote', 'Found Remote URL field.');
    $this->assertField('refresh', 'Found Refresh field.');
    $this->assertFieldByName("category[$cid]", $cid, 'Found category field.');
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
