import * as React from 'react';
import { createPortal } from 'react-dom';

import styles from './GeneralLoader.css';

export function GeneralLoader() {
  const renderLoader = () => {
    return (
      <div className={styles['container']}>
        <svg className={styles['loader']} viewBox="-2000 -1000 4000 2000">
          <path id="inf" d="M354-354A500 500 0 1 1 354 354L-354-354A500 500 0 1 0-354 354z"></path>
          <use xlinkHref="#inf" strokeDasharray="1570 5143" strokeDashoffset="6713px"></use>
        </svg>
      </div>
    );
  };
  return createPortal(renderLoader(), document.body);
}