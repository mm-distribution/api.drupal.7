# TranslationTestCase::testLanguageSwitcherBlockIntegration()

- **Type:** Method
- **File:** [`modules/translation/translation.test`](../_file.md), lines 201–258 · [local source](../../../../../source/modules/translation/translation.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test#L201-L258)
- **Class:** [TranslationTestCase](../TranslationTestCase.md)
- **Module/theme:** translation

## Signature

```php
function testLanguageSwitcherBlockIntegration()
```

## Documentation

```text
Tests that the language switcher block alterations work as intended.
```

## Code

```php
  function testLanguageSwitcherBlockIntegration() {
    // Enable Italian to have three items in the language switcher block.
    $this->drupalLogin($this->admin_user);
    $edit = array('enabled[it]' => TRUE);
    $this->drupalPost('admin/config/regional/language', $edit, t('Save configuration'));
    $this->drupalLogin($this->translator);

    // Create a Basic page in English.
    $type = 'block-locale';
    $node = $this->createPage($this->randomName(), $this->randomName(), 'en');
    $this->assertLanguageSwitchLinks($node, $node, TRUE, $type);
    $this->assertLanguageSwitchLinks($node, $this->emptyNode('es'), TRUE, $type);
    $this->assertLanguageSwitchLinks($node, $this->emptyNode('it'), TRUE, $type);

    // Create the Spanish translation.
    $translation_es = $this->createTranslation($node, $this->randomName(), $this->randomName(), 'es');
    $this->assertLanguageSwitchLinks($node, $node, TRUE, $type);
    $this->assertLanguageSwitchLinks($node, $translation_es, TRUE, $type);
    $this->assertLanguageSwitchLinks($node, $this->emptyNode('it'), TRUE, $type);

    // Create the Italian translation.
    $translation_it = $this->createTranslation($node, $this->randomName(), $this->randomName(), 'it');
    $this->assertLanguageSwitchLinks($node, $node, TRUE, $type);
    $this->assertLanguageSwitchLinks($node, $translation_es, TRUE, $type);
    $this->assertLanguageSwitchLinks($node, $translation_it, TRUE, $type);

    // Create a language neutral node and check that the language switcher is
    // left untouched.
    $node2 = $this->createPage($this->randomName(), $this->randomName(), LANGUAGE_NONE);
    $node2_en = (object) array('nid' => $node2->nid, 'language' => 'en');
    $node2_es = (object) array('nid' => $node2->nid, 'language' => 'es');
    $node2_it = (object) array('nid' => $node2->nid, 'language' => 'it');
    $this->assertLanguageSwitchLinks($node2_en, $node2_en, TRUE, $type);
    $this->assertLanguageSwitchLinks($node2_en, $node2_es, TRUE, $type);
    $this->assertLanguageSwitchLinks($node2_en, $node2_it, TRUE, $type);

    // Disable translation support to check that the language switcher is left
    // untouched only for new nodes.
    $this->drupalLogin($this->admin_user);
    $edit = array('language_content_type' => 0);
    $this->drupalPost('admin/structure/types/manage/page', $edit, t('Save content type'));
    $this->drupalLogin($this->translator);

    // Existing translations trigger alterations even if translation support is
    // disabled.
    $this->assertLanguageSwitchLinks($node, $node, TRUE, $type);
    $this->assertLanguageSwitchLinks($node, $translation_es, TRUE, $type);
    $this->assertLanguageSwitchLinks($node, $translation_it, TRUE, $type);

    // Check that new nodes with a language assigned do not trigger language
    // switcher alterations when translation support is disabled.
    $node = $this->createPage($this->randomName(), $this->randomName());
    $node_es = (object) array('nid' => $node->nid, 'language' => 'es');
    $node_it = (object) array('nid' => $node->nid, 'language' => 'it');
    $this->assertLanguageSwitchLinks($node, $node, TRUE, $type);
    $this->assertLanguageSwitchLinks($node, $node_es, TRUE, $type);
    $this->assertLanguageSwitchLinks($node, $node_it, TRUE, $type);
  }
```

---
_Drupal 7.103 · [modules/translation/translation.test](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.test) · Licensed GPL-2.0-or-later (see LICENSE)._
