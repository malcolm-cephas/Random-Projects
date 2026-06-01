export const getData = (key) => {
  if (typeof window === 'undefined' || !window.localStorage) return null;

  try {
    const data = localStorage.getItem(key);
    return data ? JSON.parse(data) : null;
  } catch (err) {
    console.error(`Error getting item ${key} from localStorage`, err);
    return null;
  }
};

export const storeData = (key, item) => {
  if (typeof window === 'undefined' || !window.localStorage) return;

  try {
    localStorage.setItem(key, JSON.stringify(item));
  } catch (err) {
    console.error(`Error storing item ${key} to localStorage`, err);
  }
};
