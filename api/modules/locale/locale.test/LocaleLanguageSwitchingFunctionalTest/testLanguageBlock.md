# LocaleLanguageSwitchingFunctionalTest::testLanguageBlock()

- **Type:** Method
- **File:** [`modules/locale/locale.test`](../_file.md), lines 1628–1679 · [local source](../../../../../source/modules/locale/locale.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test#L1628-L1679)
- **Class:** [LocaleLanguageSwitchingFunctionalTest](../LocaleLanguageSwitchingFunctionalTest.md)
- **Module/theme:** locale

## Signature

```php
function testLanguageBlock()
```

## Documentation

```text
Functional tests for the language switcher block.
```

## Code

```php
  function testLanguageBlock() {
    // Enable the language switching block.
    $language_type = LANGUAGE_TYPE_INTERFACE;
    $edit = array(
      "blocks[locale_{$language_type}][region]" => 'sidebar_first',
    );
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));

    // Add language.
    $edit = array(
      'langcode' => 'fr',
    );
    $this->drupalPost('admin/config/regional/language/add', $edit, t('Add language'));

    // Enable URL language detection and selection.
    $edit = array('language[enabled][locale-url]' => '1');
    $this->drupalPost('admin/config/regional/language/configure', $edit, t('Save settings'));

    // Assert that the language switching block is displayed on the frontpage.
    $this->drupalGet('');
    $this->assertText(t('Languages'), 'Language switcher block found.');

    // Assert that only the current language is marked as active.
    list($language_switcher) = $this->xpath('//div[@id=:id]/div[@class="content"]', array(':id' => 'block-locale-' . $language_type));
    $links = array(
      'active' => array(),
      'inactive' => array(),
    );
    $anchors = array(
      'active' => array(),
      'inactive' => array(),
    );
    foreach ($language_switcher->ul->li as $link) {
      $classes = explode(" ", (string) $link['class']);
      list($language) = array_intersect($classes, array('en', 'fr'));
      if (in_array('active', $classes)) {
        $links['active'][] = $language;
      }
      else {
        $links['inactive'][] = $language;
      }
      $anchor_classes = explode(" ", (string) $link->a['class']);
      if (in_array('active', $anchor_classes)) {
        $anchors['active'][] = $language;
      }
      else {
        $anchors['inactive'][] = $language;
      }
    }
    $this->assertIdentical($links, array('active' => array('en'), 'inactive' => array('fr')), 'Only the current language list item is marked as active on the language switcher block.');
    $this->assertIdentical($anchors, array('active' => array('en'), 'inactive' => array('fr')), 'Only the current language anchor is marked as active on the language switcher block.');
  }
```

---
_Drupal 7.103 · [modules/locale/locale.test](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.test) · Licensed GPL-2.0-or-later (see LICENSE)._
