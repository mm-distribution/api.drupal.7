# Taxonomy indexing

- **Topic id:** `taxonomy_index`
- **Defined in:** [`modules/taxonomy/taxonomy.module`](../modules/taxonomy/taxonomy.module/_file.md), line 1879 · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L1879)

## Documentation

```text
@defgroup taxonomy_index Taxonomy indexing
@{
Functions to maintain taxonomy indexing.

Taxonomy uses default field storage to store canonical relationships
between terms and fieldable entities. However its most common use case
requires listing all content associated with a term or group of terms
sorted by creation date. To avoid slow queries due to joining across
multiple node and field tables with various conditions and order by criteria,
we maintain a denormalized table with all relationships between terms,
published nodes and common sort criteria such as sticky and created.
This is used as a lookup table by taxonomy_select_nodes(). When using other
field storage engines or alternative methods of denormalizing this data
you should set the variable 'taxonomy_maintain_index_table' to FALSE
to avoid unnecessary writes in SQL.
```

## Members (derived, 7)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [taxonomy_build_node_index()](../modules/taxonomy/taxonomy.module/taxonomy_build_node_index.md) (function) — Builds and inserts taxonomy index entries for a given node.
- [taxonomy_delete_node_index()](../modules/taxonomy/taxonomy.module/taxonomy_delete_node_index.md) (function) — Deletes taxonomy index entries for a given node.
- [taxonomy_field_presave()](../modules/taxonomy/taxonomy.module/taxonomy_field_presave.md) (function) — Implements hook_field_presave().
- [taxonomy_node_delete()](../modules/taxonomy/taxonomy.module/taxonomy_node_delete.md) (function) — Implements hook_node_delete().
- [taxonomy_node_insert()](../modules/taxonomy/taxonomy.module/taxonomy_node_insert.md) (function) — Implements hook_node_insert().
- [taxonomy_node_update()](../modules/taxonomy/taxonomy.module/taxonomy_node_update.md) (function) — Implements hook_node_update().
- [taxonomy_taxonomy_term_delete()](../modules/taxonomy/taxonomy.module/taxonomy_taxonomy_term_delete.md) (function) — Implements hook_taxonomy_term_delete().

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
