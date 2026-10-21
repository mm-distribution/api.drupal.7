# ImportOPMLTestCase::submitImportForm()

- **Type:** Method
- **File:** [`modules/aggregator/aggregator.test`](../_file.md), lines 796–851 · [local source](../../../../../source/modules/aggregator/aggregator.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test#L796-L851)
- **Class:** [ImportOPMLTestCase](../ImportOPMLTestCase.md)
- **Module/theme:** aggregator

## Signature

```php
function submitImportForm()
```

## Documentation

```text
Submits form with invalid, empty, and valid OPML files.
```

## Code

```php
  function submitImportForm() {
    $before = db_query('SELECT COUNT(*) FROM {aggregator_feed}')->fetchField();

    $form['files[upload]'] = $this->getInvalidOpml();
    $this->drupalPost('admin/config/services/aggregator/add/opml', $form, t('Import'));
    $this->assertText(t('No new feed has been added.'), 'Attempting to upload invalid XML.');

    $edit = array('remote' => file_create_url($this->getEmptyOpml()));
    $this->drupalPost('admin/config/services/aggregator/add/opml', $edit, t('Import'));
    $this->assertText(t('No new feed has been added.'), 'Attempting to load empty OPML from remote URL.');

    $after = db_query('SELECT COUNT(*) FROM {aggregator_feed}')->fetchField();
    $this->assertEqual($before, $after, 'No feeds were added during the two last form submissions.');

    db_delete('aggregator_feed')->execute();
    db_delete('aggregator_category')->execute();
    db_delete('aggregator_category_feed')->execute();

    $category = $this->randomName(10);
    db_insert('aggregator_category')
      ->fields(array(
        'cid' => 1,
        'title' => $category,
        'description' => '',
      ))
      ->execute();

    $feeds[0] = $this->getFeedEditArray();
    $feeds[1] = $this->getFeedEditArray();
    $feeds[2] = $this->getFeedEditArray();
    $edit = array(
      'files[upload]' => $this->getValidOpml($feeds),
      'refresh'       => '900',
      'category[1]'   => $category,
    );
    $this->drupalPost('admin/config/services/aggregator/add/opml', $edit, t('Import'));
    $this->assertRaw(t('A feed with the URL %url already exists.', array('%url' => $feeds[0]['url'])), 'Verifying that a duplicate URL was identified');
    $this->assertRaw(t('A feed named %title already exists.', array('%title' => $feeds[1]['title'])), 'Verifying that a duplicate title was identified');

    $after = db_query('SELECT COUNT(*) FROM {aggregator_feed}')->fetchField();
    $this->assertEqual($after, 2, 'Verifying that two distinct feeds were added.');

    $feeds_from_db = db_query("SELECT f.title, f.url, f.refresh, cf.cid FROM {aggregator_feed} f LEFT JOIN {aggregator_category_feed} cf ON f.fid = cf.fid");
    $refresh = $category = TRUE;
    foreach ($feeds_from_db as $feed) {
      $title[$feed->url] = $feed->title;
      $url[$feed->title] = $feed->url;
      $category = $category && $feed->cid == 1;
      $refresh = $refresh && $feed->refresh == 900;
    }

    $this->assertEqual($title[$feeds[0]['url']], $feeds[0]['title'], 'First feed was added correctly.');
    $this->assertEqual($url[$feeds[1]['title']], $feeds[1]['url'], 'Second feed was added correctly.');
    $this->assertTrue($refresh, 'Refresh times are correct.');
    $this->assertTrue($category, 'Categories are correct.');
  }
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.test](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.test) · Licensed GPL-2.0-or-later (see LICENSE)._
