# locale_update_7004()

- **Type:** Function
- **File:** [`modules/locale/locale.install`](_file.md), lines 148–202 · [local source](../../../../source/modules/locale/locale.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install#L148-L202)
- **Module/theme:** locale
- **Topics:** [updates-7.x-extra](../../../topics/updates-7.x-extra.md)

## Signature

```php
function locale_update_7004()
```

## Documentation

```text
Remove duplicates in {locales_source}.
```

## Code

```php
function locale_update_7004() {
  // Look up all duplicates. For each set of duplicates, we select the row
  // with the lowest lid as the "master" that will be preserved.
  $result_source = db_query("SELECT MIN(lid) AS lid, source, context FROM {locales_source} WHERE textgroup = 'default' GROUP BY source, context HAVING COUNT(*) > 1");

  $conflict = FALSE;
  foreach ($result_source as $source) {
    // Find all rows in {locales_target} that are translations of the same
    // string (incl. context).
    $result_target = db_query("SELECT t.lid, t.language, t.plural, t.translation FROM {locales_source} s JOIN {locales_target} t ON s.lid = t.lid WHERE s.source = :source AND s.context = :context AND s.textgroup = 'default' ORDER BY lid", array(
      ':source' => $source->source,
      ':context' => $source->context,
    ));

    $translations = array();
    $keep_lids = array($source->lid);
    foreach ($result_target as $target) {
      if (!isset($translations[$target->language])) {
        $translations[$target->language] = $target->translation;
        if ($target->lid != $source->lid) {
          // Move translation to the master lid.
          db_query('UPDATE {locales_target} SET lid = :new_lid WHERE lid = :old_lid', array(
            ':new_lid' => $source->lid,
            ':old_lid' => $target->lid));
        }
      }
      elseif ($translations[$target->language] == $target->translation) {
        // Delete duplicate translation.
        db_query('DELETE FROM {locales_target} WHERE lid = :lid AND language = :language', array(
          ':lid' => $target->lid,
          ':language' => $target->language));
      }
      else {
        // The same string is translated into several different strings in one
        // language. We do not know which is the preferred, so we keep them all.
        $keep_lids[] = $target->lid;
        $conflict = TRUE;
      }
    }

    // Delete rows in {locales_source} that are no longer referenced from
    // {locales_target}.
    db_delete('locales_source')
      ->condition('source', $source->source)
      ->condition('context', $source->context)
      ->condition('textgroup', 'default')
      ->condition('lid', $keep_lids, 'NOT IN')
      ->execute();
  }

  if ($conflict) {
    $url = 'http://drupal.org/node/746240';
    drupal_set_message('Your {locales_source} table contains duplicates that could not be removed automatically. See <a href="' . $url .'" target="_blank">' . $url . '</a> for more information.', 'warning');
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.install](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.install) · Licensed GPL-2.0-or-later (see LICENSE)._
