# _locale_translate_seek()

- **Type:** Function
- **File:** [`includes/locale.inc`](_file.md), lines 1888–1983 · [local source](../../../source/includes/locale.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc#L1888-L1983)
- **Topics:** [locale-api-seek](../../topics/locale-api-seek.md)

## Signature

```php
function _locale_translate_seek()
```

## Documentation

```text
Perform a string search and display results in a table
```

## Code

```php
function _locale_translate_seek() {
  $output = '';

  // We have at least one criterion to match
  if (!($query = _locale_translate_seek_query())) {
    $query = array(
      'translation' => 'all',
      'group' => 'all',
      'language' => 'all',
      'string' => '',
    );
  }

  $sql_query = db_select('locales_source', 's');

  $limit_language = NULL;
  if ($query['language'] != 'en' && $query['language'] != 'all') {
    $sql_query->leftJoin('locales_target', 't', "t.lid = s.lid AND t.language = :langcode", array(':langcode' => $query['language']));
    $limit_language = $query['language'];
  }
  else {
    $sql_query->leftJoin('locales_target', 't', 't.lid = s.lid');
  }

  $sql_query->fields('s', array('source', 'location', 'context', 'lid', 'textgroup'));
  $sql_query->fields('t', array('translation', 'language'));

  // Compute LIKE section.
  switch ($query['translation']) {
    case 'translated':
      $sql_query->condition('t.translation', '%' . db_like($query['string']) . '%', 'LIKE');
      $sql_query->orderBy('t.translation', 'DESC');
      break;
    case 'untranslated':
      $sql_query->condition(db_and()
        ->condition('s.source', '%' . db_like($query['string']) . '%', 'LIKE')
        ->isNull('t.translation')
      );
      $sql_query->orderBy('s.source');
      break;
    case 'all' :
    default:
      $condition = db_or()
        ->condition('s.source', '%' . db_like($query['string']) . '%', 'LIKE');
      if ($query['language'] != 'en') {
        // Only search in translations if the language is not forced to English.
        $condition->condition('t.translation', '%' . db_like($query['string']) . '%', 'LIKE');
      }
      $sql_query->condition($condition);
      break;
  }

  // Add a condition on the text group.
  if (!empty($query['group']) && $query['group'] != 'all') {
    $sql_query->condition('s.textgroup', $query['group']);
  }

  $sql_query = $sql_query->extend('PagerDefault')->limit(50);
  $locales = $sql_query->execute();

  $groups = module_invoke_all('locale', 'groups');
  $header = array(t('Text group'), t('String'), t('Context'), ($limit_language) ? t('Language') : t('Languages'), array('data' => t('Operations'), 'colspan' => '2'));

  $strings = array();
  foreach ($locales as $locale) {
    if (!isset($strings[$locale->lid])) {
      $strings[$locale->lid] = array(
        'group' => $locale->textgroup,
        'languages' => array(),
        'location' => $locale->location,
        'source' => $locale->source,
        'context' => $locale->context,
      );
    }
    if (isset($locale->language)) {
      $strings[$locale->lid]['languages'][$locale->language] = $locale->translation;
    }
  }

  $rows = array();
  foreach ($strings as $lid => $string) {
    $rows[] = array(
      $groups[$string['group']],
      array('data' => check_plain(truncate_utf8($string['source'], 150, FALSE, TRUE)) . '<br /><small>' . $string['location'] . '</small>'),
      $string['context'],
      array('data' => _locale_translate_language_list($string, $limit_language), 'align' => 'center'),
      array('data' => l(t('edit'), "admin/config/regional/translate/edit/$lid", array('query' => drupal_get_destination())), 'class' => array('nowrap')),
      array('data' => l(t('delete'), "admin/config/regional/translate/delete/$lid", array('query' => drupal_get_destination())), 'class' => array('nowrap')),
    );
  }

  $output .= theme('table', array('header' => $header, 'rows' => $rows, 'empty' => t('No strings available.')));
  $output .= theme('pager');

  return $output;
}
```

---
_Drupal 7.103 · [includes/locale.inc](https://github.com/drupal/drupal/blob/7.103/includes/locale.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
