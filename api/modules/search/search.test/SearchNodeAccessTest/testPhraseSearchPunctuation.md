# SearchNodeAccessTest::testPhraseSearchPunctuation()

- **Type:** Method
- **File:** [`modules/search/search.test`](../_file.md), lines 2069–2095 · [local source](../../../../../source/modules/search/search.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test#L2069-L2095)
- **Class:** [SearchNodeAccessTest](../SearchNodeAccessTest.md)
- **Module/theme:** search

## Signature

```php
function testPhraseSearchPunctuation()
```

## Documentation

```text
Tests that search works with punctuation and HTML entities.
```

## Code

```php
  function testPhraseSearchPunctuation() {
    $node = $this->drupalCreateNode(array('body' => array(LANGUAGE_NONE => array(array('value' => "The bunny's ears were fuzzy.")))));
    $node2 = $this->drupalCreateNode(array('body' => array(LANGUAGE_NONE => array(array('value' => 'Dignissim Aliquam &amp; Quieligo meus natu quae quia te. Damnum&copy; erat&mdash; neo pneum. Facilisi feugiat ibidem ratis.')))));

    // Update the search index.
    module_invoke_all('update_index');
    search_update_totals();

    // Refresh variables after the treatment.
    $this->refreshVariables();

    // Submit a phrase wrapped in double quotes to include the punctuation.
    $edit = array('keys' => '"bunny\'s"');
    $this->drupalPost('search/node', $edit, t('Search'));
    $this->assertText($node->title);

    // Search for "&" and verify entities are not broken up in the output.
    $edit = array('keys' => '&');
    $this->drupalPost('search/node', $edit, t('Search'));
    $this->assertNoRaw('<strong>&</strong>amp;');
    $this->assertText('You must include at least one positive keyword');

    $edit = array('keys' => '&amp;');
    $this->drupalPost('search/node', $edit, t('Search'));
    $this->assertNoRaw('<strong>&</strong>amp;');
    $this->assertText('You must include at least one positive keyword');
  }
```

---
_Drupal 7.103 · [modules/search/search.test](https://github.com/drupal/drupal/blob/7.103/modules/search/search.test) · Licensed GPL-2.0-or-later (see LICENSE)._
