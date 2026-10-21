# LocaleMultilingualFieldsFunctionalTest::testMultilingualDisplaySettings()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 2873–2896 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L2873-L2896)
- **Class:** [LocaleMultilingualFieldsFunctionalTest](../LocaleMultilingualFieldsFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testMultilingualDisplaySettings()
```

## Documentation

_No docblock in source._

## Code

```php
  function testMultilingualDisplaySettings() {
    // Create "Basic page" content.
    $langcode = LANGUAGE_NONE;
    $title_key = "title";
    $title_value = $this->randomName(8);
    $body_key = "body[$langcode][0][value]";
    $body_value = $this->randomName(16);

    // Create node to edit.
    $edit = array();
    $edit[$title_key] = $title_value;
    $edit[$body_key] = $body_value;
    $edit['language'] = 'en';
    $this->drupalPost('node/add/page', $edit, t('Save'));

    // Check that the node exists in the database.
    $node = $this->drupalGetNodeByTitle($edit[$title_key]);
    $this->assertTrue($node, 'Node found in database.');

    // Check if node body is showed.
    $this->drupalGet("node/$node->nid");
    $body = $this->xpath('//div[@id=:id]//div[@property="content:encoded"]/p', array(':id' => 'node-' . $node->nid));
    $this->assertEqual(current($body), $node->body['en'][0]['value'], 'Node body is correctly showed.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
